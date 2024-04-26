<script lang="ts">
  import Counter from './lib/Counter.svelte'
  import Loops from './lib/Loops.svelte'
  import Fetch from './lib/Fetch.svelte'
  import Card from './lib/Card.svelte'
</script>

<main>
  <div>

  <div class="card">
    <Counter />
    <Loops />
    <Fetch />
    <Card title="Hello World">
      <p>Card content</p>
    </Card>
  </div>

</main>

<style>

</style>
