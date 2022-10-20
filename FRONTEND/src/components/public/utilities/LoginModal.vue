<script setup>
    import { ref } from 'vue'
    import { useRouter } from 'vue-router'
    import axios from 'axios'
    import { useQuasar } from 'quasar'
    const $q = useQuasar()
    const showModal = ref(false)
    const usuario = ref('')
    const password = ref('')
    const isPwd = ref(true)
    const sendingForm = ref(false)
    const router = useRouter()
    const parseJwt = (token) => {
        var base64Url = token.split('.')[1];
        var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));

        return JSON.parse(jsonPayload);
    }
    const openModalLogin = ()=>{
      const tokenAccess = JSON.parse(sessionStorage.getItem('tokens'))
      if (!tokenAccess) return showModal.value = true
      console.log(parseJwt(tokenAccess.access))
      if(parseJwt(tokenAccess.access).superUser)return router.push({name:'admin'})
    }

    const LoginMethod = () => {
      sendingForm.value = true
      axios.post('http://127.0.0.1:8000/users/login/', {
        username: usuario.value,
        password: password.value
      })
      .then((response) => {
        sessionStorage.setItem('tokens',JSON.stringify(response.data))
        //JSON.parse(sessionStorage.getItem('tokens')).access || TO READ THE DATA
        if(parseJwt(response.data.access).superUser)return router.push({name:'admin'})
      })
      .catch((error) => {
        const message = error.response.data.detail
            $q.notify({
              message,
              color: 'red',
              type:'negative',
              position:'top-right',
              multiLine: true,
              timeout:3000,
              actions: [{ icon: 'close', color: 'white' }]
            })
      })
      .finally(()=>{
        sendingForm.value = false
      })
    }
     
    </script>

<template>
    <div class="q-pa-md q-gutter-sm">
      <q-btn @click="openModalLogin" class="q-mr-lg" color="primary"  no-caps label="Iniciar sesión"/>
  
      <q-dialog
      v-model="showModal"
      full-width
    >
      <q-card>
        <div class="row">
            <div class="col-xs-12 col-sm-6 col-md-4 col-xl-6 col-lg-6">
              <div class="flex items-center justify-center" style="height: 100%;">
                <div style="width: 50%;">
                  <q-form
                    @submit.prevent="LoginMethod"
                    class="q-gutter-md"
                  >
                  <q-input :disable="sendingForm" outlined v-model="usuario" label="Usuario" />
                  <q-input label="Contraseña" :disable="sendingForm" outlined v-model="password" :type="isPwd ? 'password' : 'text'">
                    <template v-slot:append>
                      <q-icon
                        :name="isPwd ? 'visibility_off' : 'visibility'"
                        class="cursor-pointer"
                        @click="isPwd = !isPwd"
                      />
                    </template>
                  </q-input>
                  <div class="text-center">
                    <q-btn label="Enviar" type="submit" color="primary" :loading="sendingForm"/>
                  </div>
                  </q-form>
                </div>
                </div>
            </div>
            <div class="col-xs-12 col-sm-6 col-md-4 col-xl-6 col-lg-6 text-center">
              <q-img
                src="https://www.columbus.edu.co/wp-content/uploads/Columbus-logo.png"
                style="max-width:500px; height: 600px;"
                fit="contain"
              >
              </q-img>
            </div>
        </div>
        <!-- <q-card-section class="q-pt-none">
            
        </q-card-section>

        <q-card-section class="q-pt-none">

        </q-card-section>

        <q-card-actions align="center" class="bg-white q-mb-md">
          
        </q-card-actions> -->
      </q-card>
    </q-dialog>
    </div>
  </template>
  
<style>
</style>
  