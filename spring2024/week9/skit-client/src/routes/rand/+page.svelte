
<script>
  let rand = "-1";
  function getRand() {
    fetch("http://127.0.0.1:5000/rand/")
      .then(d => d.text())
      .then(d => (rand = d));
  }
</script>

<h1>Your number is {rand}!</h1>
<button on:click={getRand}>Get a random number</button>