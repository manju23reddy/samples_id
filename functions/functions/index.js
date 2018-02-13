'use strict';

const functions = require('firebase-functions');

const admin = require('firebase-admin');


exports.addMessage = functions.https.onRequest((req, res) => {
// [END addMessageTrigger]
  // Grab the text parameter.
  const original = req.query.text;
  // [START adminSdkAdd]
  // Push the new message into the Realtime Database using the Firebase Admin SDK.
  return admin.firestore().collection('movements').add({original: original}).then((writeResult) => {
    // Send back a message that we've succesfully written the message
    return res.json({result: `Message with ID: ${writeResult.id} added.`});
  });
  // [END adminSdkAdd]
});


exports.monitor = functions.database.ref('/movements/{movementId}').onWrite((event) => {
	const original = event.data.val();
	console.log('new movement', event.params.movementId, original);
	
	
	
	
});
