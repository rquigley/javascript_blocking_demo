var start = new Date().getTime();

function stopTimer() {
  var end = new Date().getTime();
  return ((end - start) / 1000) + 's';
}