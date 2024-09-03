<script setup lang="ts">
useHead(  {
  script:[
    { src: 'https://telegram.org/js/telegram-web-app.js', defer: true}
  ],
})


</script>


<template>
  <div>
    <main>
      <ClientOnly>
        <slot/>
      </ClientOnly>
    </main>
  </div>
</template>

<style scoped>


</style>