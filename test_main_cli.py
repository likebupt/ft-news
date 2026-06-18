import unittest
from unittest.mock import patch

from click.testing import CliRunner

import main


class WeeklyPipelineCliTests(unittest.TestCase):
    def test_weekly_pipeline_forwards_backfill_options(self):
        runner = CliRunner()

        with (
            patch("query.weekly_digest", return_value="digest text") as weekly_digest,
            patch("site_builder.build_site", return_value="_site") as build_site,
        ):
            result = runner.invoke(
                main.cli,
                ["weekly-pipeline", "--year", "2026", "--week", "22", "--force"],
            )

        self.assertEqual(result.exit_code, 0, result.output)
        weekly_digest.assert_called_once_with(year=2026, week=22, force=True)
        build_site.assert_called_once_with()

    def test_weekly_pipeline_uses_default_previous_week(self):
        runner = CliRunner()

        with (
            patch("query.weekly_digest", return_value="digest text") as weekly_digest,
            patch("site_builder.build_site", return_value="_site") as build_site,
        ):
            result = runner.invoke(main.cli, ["weekly-pipeline"])

        self.assertEqual(result.exit_code, 0, result.output)
        weekly_digest.assert_called_once_with(year=None, week=None, force=False)
        build_site.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
