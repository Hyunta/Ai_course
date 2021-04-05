// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here. Other Firebase libraries
// are not available in the service worker.
importScripts('https://www.gstatic.com/firebasejs/8.1.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.1.1/firebase-messaging.js');

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
firebase.initializeApp({
        apiKey: "AIzaSyBC8zki1cdiavDCVmfp649WPEhycvl2Dno",
        authDomain: "test-88a0d.firebaseapp.com",
        projectId: "test-88a0d",
        storageBucket: "test-88a0d.appspot.com",
        messagingSenderId: "5045992619",
        appId: "1:5045992619:web:332a056cfabc55844fcbee",
        measurementId: "G-2GTH1XLTWS"
});

const messaging = firebase.messaging();

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
