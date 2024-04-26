<script lang="ts">
  let count: number = 0

  $: document.title = `${count}`
  $: doubled = count * 2
  $: isEven = count % 2 === 0
  const increment = () => {
    count += 1
  }
</script>

<!-- on:pointermove={(e) => count = e.clientX} -->
<button on:click={increment}>
  count is {count}
</button>

<p>{count} x 2 = {doubled}</p>
<p>
  {count} is

  {#if isEven}
  even
  {:else}
  odd
  {/if}
</p>
