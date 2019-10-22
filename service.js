const OracleBot = require('@oracle/bots-node-sdk');
const { WebhookClient, WebhookEvent } = OracleBot.Middleware;
const { spawn } = require('child_process');

const ROUTES_PATH = '/home/pi/Antonia/routes/routes';

const routes = require(ROUTES_PATH);
const secretKey = require(routes.secretKey);

module.exports = (app) => {
  const logger = console;
  // initialize the application with OracleBot
  OracleBot.init(app, {
    logger,
  });

  // add webhook integration
  const webhook = new WebhookClient({
    channel: {
      url: secretKey.url,
      secret: secretKey.secret,
    }
  });

  // Add webhook event handlers.
  webhook
    .on(WebhookEvent.ERROR, err => logger.error('Error:', err.message))
    .on(WebhookEvent.MESSAGE_SENT, message => logger.info('Message to bot:', message))
    .on(WebhookEvent.MESSAGE_RECEIVED, message => {
      // message was received from bot. forward to messaging client.
      logger.info('Message from bot:', message);
      console.log(MESSAGE_RECEIVED);
      // TODO: implement send to client...
      logger.info('MessageReceived: ', MESSAGE_RECEIVED);
    });

  // Create endpoint for bot webhook channel configurtion (Outgoing URI)
  // NOTE: webhook.receiver also supports using a callback as a replacement for WebhookEvent.MESSAGE_RECEIVED.
  //  - Useful in cases where custom validations, etc need to be performed.

  // Integrate with messaging client according to their specific SDKs, etc.
  app.post('/test/message', (req, res) => {
    const { user, text } = req.body;
    // construct message to bot from the client message format
    const MessageModel = webhook.MessageModel();
    const message = {
      userId: user,
      messagePayload: MessageModel.textConversationMessage(text)
    };

    // send to bot webhook channel
    webhook.send(message)
      .then(() => res.send('ok'), e => res.status(400).end(e.message));
  });

    app.post('/', (req, res) => {
      const response = webhook.receiver();
      res.set('Content-Type', 'application/json');

      res.send(response);
      var resjson = res.req.body;
      console.log(resjson.messagePayload.text);
      console.log("* NODE DEBUG: START PY TTS *");
      var spawn = require("child_process").spawn;
      var process = spawn(routes.pythonExecutable, [routes.textToSpeechScript, resjson.messagePayload.text]);
      process.stdout.on('data', (data) => { 
          console.log(data.toString()); 
      });
      console.log("* NODE DEBUG: END PY TTS *");
    });
}
