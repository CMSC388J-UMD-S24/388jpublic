<script lang="ts">
  const promise = Promise.resolve(69);
</script>

{#await promise}
loading
{:then number}
<p>The number is {number}</p>
{:catch error}
error
{/await}
