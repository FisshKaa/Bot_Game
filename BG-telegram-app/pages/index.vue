<script setup lang="ts">
const { MainButton, useWebAppPopup, useWebApp} = await import('vue-tg')

const { showAlert } = useWebAppPopup()

const { initDataUnsafe } = useWebApp()
</script>


<template>
  <section>
    <h1>Hello telegram!</h1>
    <h2> Your name is {{ initDataUnsafe.user?.username }}</h2>

    <MainButton text="Привет главная кнопка" color="rgba(0, 191, 111, 1)" @click="() => showAlert('Наше сообщение') "/>
  </section>
</template>

<style scoped>


</style>