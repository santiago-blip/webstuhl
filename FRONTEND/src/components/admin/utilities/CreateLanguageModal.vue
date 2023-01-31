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
        optionsLanguage:{
            type:Array
        },
        languageData :{ 
            type:Object
            }
    })
    const loading = ref(false)
    const data = ref(props.languageData)
    
    const toDelete = []
    const SubmitData = ()=>{
        loading.value = true
        let request = null
        if(toDelete.length)data.value.toDelete = toDelete
        if(!data.value.id){
            const url = 'http://127.0.0.1:8000/vacancies/master/languages/'
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
                data.value = {language_name:""}
                return emit('submittedData')
            })
        
    }
    const onChange = (value,action)=>{
        if(action == 'add'){
            if(toDelete.indexOf(value.value.id)>=0)toDelete.splice(toDelete.indexOf(value.value.id),1)
        }
        if(action == 'remove'){
            // if(toAdd.indexOf(value.value.id)>=0)toAdd.splice(toAdd.indexOf(value.value.id),1)
            if(!toDelete.find(x=>x==value.value.id))toDelete.push(value.value.id)
        }
        console.log(toDelete)
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
                    v-model="data.language_name"
                    :label="$t('languages')"
                    lazy-rules
                    :rules="[ val => val && val !== '' || 'Please type something']"
                    :disabled="loading"
                    />
                <q-select outlined  v-model="data.levels" multiple :options="optionsLanguage" :option-label="opt =>opt.language_level" :label="$t('level')" class="q-mt-sm" @add="val => onChange(val,'add')" @remove="val => onChange(val,'remove')"/>
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