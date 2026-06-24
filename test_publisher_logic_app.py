import unittest
from unittest.mock import MagicMock, Mock, patch

import httpx

import publisher


class PublisherLogicAppTests(unittest.TestCase):
    def test_send_email_posts_logic_app_payload(self):
        response = Mock(status_code=202)
        response.raise_for_status.return_value = None

        client = MagicMock()
        client.__enter__.return_value = client
        client.post.return_value = response

        with (
            patch.object(publisher, "LOGIC_APP_URL", "https://logic.example/invoke"),
            patch.object(
                publisher,
                "EMAIL_RECIPIENTS",
                "one@example.com;two@example.com",
            ),
            patch.object(publisher, "EMAIL_SENDER", "sender@example.com"),
            patch.object(publisher.httpx, "Client", return_value=client),
        ):
            sent = publisher.send_email(
                "# Digest\n\n- **Important** [link](https://example.com)",
                "Subject",
            )

        self.assertTrue(sent)
        client.post.assert_called_once()
        call_kwargs = client.post.call_args.kwargs
        self.assertEqual(call_kwargs["json"]["subject"], "Subject")
        self.assertEqual(call_kwargs["json"]["to"], "one@example.com;two@example.com")
        self.assertEqual(call_kwargs["json"]["from"], "sender@example.com")
        self.assertIn("<h1", call_kwargs["json"]["body"])
        self.assertIn("<strong>Important</strong>", call_kwargs["json"]["body"])
        self.assertEqual(call_kwargs["headers"], {"Content-Type": "application/json"})

    def test_send_email_requires_logic_app_url(self):
        with (
            patch.object(publisher, "LOGIC_APP_URL", ""),
            patch.object(publisher, "EMAIL_RECIPIENTS", "one@example.com"),
            patch.object(publisher.httpx, "Client") as client_class,
        ):
            sent = publisher.send_email("digest")

        self.assertFalse(sent)
        client_class.assert_not_called()

    def test_send_email_requires_recipients(self):
        with (
            patch.object(publisher, "LOGIC_APP_URL", "https://logic.example/invoke"),
            patch.object(publisher, "EMAIL_RECIPIENTS", ""),
            patch.object(publisher.httpx, "Client") as client_class,
        ):
            sent = publisher.send_email("digest")

        self.assertFalse(sent)
        client_class.assert_not_called()

    def test_send_email_returns_false_for_http_status_error(self):
        request = httpx.Request("POST", "https://logic.example/invoke")
        response = httpx.Response(500, request=request, text="failed")

        client = MagicMock()
        client.__enter__.return_value = client
        client.post.return_value = response

        with (
            patch.object(publisher, "LOGIC_APP_URL", "https://logic.example/invoke"),
            patch.object(publisher, "EMAIL_RECIPIENTS", "one@example.com"),
            patch.object(publisher, "EMAIL_SENDER", ""),
            patch.object(publisher.httpx, "Client", return_value=client),
        ):
            sent = publisher.send_email("digest")

        self.assertFalse(sent)


if __name__ == "__main__":
    unittest.main()