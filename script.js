fetch(
  "https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelId=UC29BKw2DaNMQe2B90QRVCNw&order=searchSortUnspecified&q=Sex%2C%20Power%2C%20Riches%20and%20Materialism%20%7C%20Billy%20Graham%20Classics&key=AIzaSyAhOvT2_SJl4lc1us3Mj8e4brz_qwvH8Fs"
)
  //what is wrong with the bottom code?
  //The fetch call does not have a .then() to handle the response
  .then((result) => {
    return result.json();
  })
  .then((data) => {
    console.log(data);
    let videos = data.items;
    let videoContainer = document.querySelector(".youtube-container");
    for (let video of videos) {
      videoContainer.innerHTML += `
      <img src="${video.snippet.thumbnails.high.url}">
      `;
    }
  });
