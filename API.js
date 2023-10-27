const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`API listening at http://localhost:${port}`);
});




const {google} = require('googleapis');
const youtube = google.youtube('v3');

// Set up the OAuth2 client
const oauth2Client = new google.auth.OAuth2(
  YOUR_CLIENT_ID,
  YOUR_CLIENT_SECRET,
  YOUR_REDIRECT_URL
);

// Authorize the client with the access token
oauth2Client.setCredentials({
  access_token: YOUR_ACCESS_TOKEN
});

// Define the search query
const searchQuery = 'cats';

// Call the YouTube API to search for videos
youtube.search.list({
  auth: oauth2Client,
  part: 'id,snippet',
  q: searchQuery
}).then(response => {
  const videos = response.data.items;
  console.log(`Found ${videos.length} videos for "${searchQuery}"`);
  videos.forEach(video => {
    console.log(`Title: ${video.snippet.title}`);
    console.log(`URL: https://www.youtube.com/watch?v=${video.id.videoId}`);
  });
}).catch(err => {
  console.error('Error searching for videos:', err);
});