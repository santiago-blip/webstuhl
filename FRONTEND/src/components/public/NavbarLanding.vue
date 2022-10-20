<script setup>
  import { ref } from 'vue'
  import LoginModal from '@/components/public/utilities/LoginModal.vue'

  </script>


<template>
    <q-toolbar class="text-primary">
      <q-toolbar-title class="text-weight-bold">
        Vacantes TCS
      </q-toolbar-title>
      <LoginModal></LoginModal>
    </q-toolbar>
</template>