<template>
  <div id="app">
    <div class="circle"></div>
  </div>
</template>

<script>
export default {
  mounted() {
    // Agregamos una clase "move" al círculo después de que el componente se monte
    const circle = document.querySelector('.circle');
    circle.classList.add('move');
  },
};
</script>

<style scoped>
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f0f0;
}

.circle {
  width: 50px;
  height: 50px;
  background-color: #007bff;
  border-radius: 50%;
  position: relative;
  animation: moveCircle 4s linear infinite;
}

@keyframes moveCircle {
  0% {
    left: 0;
  }
  50% {
    left: calc(100% - 50px);
  }
  100% {
    left: 0;
  }
}
</style>
