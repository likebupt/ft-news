import inspect
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import httpx

import map_reduce
import query


class _SuccessfulResponse:
    status_code = 200
    text = "{}"

    def json(self):
        return {
            "output": [
                {
                    "type": "message",
                    "content": [
                        {"type": "output_text", "text": "retry succeeded"}
                    ],
                }
            ]
        }

    def raise_for_status(self):
        raise AssertionError("raise_for_status should not be called for success")


class MapReduceResilienceTests(unittest.TestCase):
    def test_llm_request_errors_are_retried(self):
        attempts = []

        def fake_post(*args, **kwargs):
            attempts.append(kwargs["json"])
            if len(attempts) == 1:
                raise httpx.RequestError("connection reset")
            return _SuccessfulResponse()

        with (
            patch.object(map_reduce.httpx, "post", side_effect=fake_post),
            patch.object(map_reduce.time, "sleep", return_value=None),
        ):
            text = map_reduce._call_llm("instructions", "input", max_tokens=123)

        self.assertEqual(text, "retry succeeded")
        self.assertEqual(len(attempts), 2)
        self.assertEqual(attempts[-1]["max_output_tokens"], 123)

    def test_weekly_single_partial_skips_reduce_call(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with (
                patch.object(map_reduce, "DATA_DIR", Path(temp_dir)),
                patch.object(map_reduce, "_map_chunks_parallel", return_value=["single partial"]),
                patch.object(map_reduce, "merge_summaries") as merge_summaries,
            ):
                digest = map_reduce.map_reduce_weekly([[{"id": 1}]], 2026, 22)

            self.assertEqual(digest, "single partial")
            merge_summaries.assert_not_called()
            out_file = Path(temp_dir) / "2026" / "week-22" / "weekly-digest.md"
            self.assertEqual(out_file.read_text(encoding="utf-8"), "single partial")

    def test_digest_defaults_use_smaller_chunks(self):
        self.assertEqual(
            inspect.signature(query.daily_digest).parameters["chunk_size"].default,
            10,
        )
        self.assertEqual(
            inspect.signature(query.weekly_digest).parameters["chunk_size"].default,
            10,
        )

    def test_article_excerpt_is_trimmed_for_llm_payload(self):
        formatted = map_reduce._format_chunk([
            {
                "source_name": "Example",
                "category": "research",
                "title": "Long article",
                "url": "https://example.com/article",
                "published": "2026-06-18T00:00:00+00:00",
                "summary": "x" * 500,
            }
        ])

        self.assertIn("Excerpt: " + ("x" * 250), formatted)
        self.assertNotIn("x" * 251, formatted)


if __name__ == "__main__":
    unittest.main()