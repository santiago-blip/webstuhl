<script setup>
import { ref } from 'vue';
import axios from 'axios'
import { Loading, useQuasar } from 'quasar'
    
    const $q = useQuasar()
    const emit = defineEmits(['closeModalNewLanguage','submittedData'])
    const props = defineProps({
        showModalNewLanguage:{
            type:Boolean,
            default:false
        },
        languageData :{ 
            type:Object
            }
    })
    const loading = ref(false)
    const data = ref(props.languageData)
    const SubmitData = ()=>{
        loading.value = true
        let request = null
        if(!data.value.id){
            const url = 'http://127.0.0.1:8000/vacancies/master/languages-level/'
            request = axios.post(url,data.value)
        }else{
            const url = data.value.url
            request = axios.put(url,data.value)
        }
            request
            .then(response=>{
                        $q.notify({
                                message:response.data.response,
                                color: 'green',
                                type:'positive',
                                position:'top-right',
                                multiLine: true,
                                timeout:3000,
                                actions: [{ icon: 'close', color: 'white' }]
                            })  
            })
            .catch(error=>{
                        $q.notify({
                                message:error.message,
                                color: 'red',
                                type:'negative',
                                position:'top-right',
                                multiLine: true,
                                timeout:3000,
                                actions: [{ icon: 'close', color: 'white' }]
                            })
            })
            .finally(()=>{
                loading.value = false
                data.value = {language_level:""}
                return emit('submittedData')
            })
        
    }
</script>
<template>
    
    <q-dialog v-model="showModalNewLanguage" persistent>
        <q-card>
            <div class="q-pa-md">
                <q-form
                @submit.prevent="SubmitData"
                class="q-gutter-md"
                >
                <q-input
                    outlined
                    v-model="data.language_level"
                    :label="$t('languages')"
                    lazy-rules
                    :rules="[ val => val && val !== '' || 'Please type something']"
                    :disabled="loading"
                    />
                <div class="text-center">
                    <q-btn label="Submit" type="submit" color="primary" :loading="loading"/>
                </div>
                </q-form>

                </div>
        <q-card-actions align="right">
          <q-btn flat :label="$t('close')" color="primary" no-caps @click="emit('closeModalNewLanguage')"/>
        </q-card-actions>
        </q-card>
    </q-dialog>
</template>
<style scoped>
</style>