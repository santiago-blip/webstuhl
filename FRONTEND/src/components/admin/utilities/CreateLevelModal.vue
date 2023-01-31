<script setup>
import { ref } from 'vue';
import axios from 'axios'
import { Loading, useQuasar } from 'quasar'
    
    const $q = useQuasar()
    const emit = defineEmits(['closeModalLevel','submittedData'])
    const props = defineProps({
        showModalNewLevel:{
            type:Boolean,
            default:false
        },
        levelData :{ 
            type:Object
        },
        optionsArea:{
            type:Array
        }
    })
    const toAdd = []
    const toDelete = []
    const loading = ref(false)
    const data = ref(props.levelData)
    const SubmitData = ()=>{
        loading.value = true
        let request = null
        if(toDelete.length)data.value.toDelete = toDelete
        if(!data.value.id){
            const url = 'http://127.0.0.1:8000/vacancies/master/levels/'
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
                data.value = {level_name:"",level_description:""}
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
    }
</script>
<template>
    
    <q-dialog v-model="showModalNewLevel" persistent>
        <q-card>
            <div class="q-pa-md" style="width: 500px;">
                <q-form
                @submit.prevent="SubmitData"
                class="q-gutter-md"
                >
                <q-input
                    outlined
                    v-model="data.level_name"
                    :label="$t('levelName')"
                    lazy-rules
                    :rules="[ val => val && val !== '' || 'Please type something']"
                    :disabled="loading"
                    />
                <q-input  :disabled="loading" outlined  v-model="data.level_description" autogrow :label="$t('levelDescription')"
                lazy-rules
                    :rules="[
                    val => val !== null && val !== '' || 'Please type something',
                    ]"
                />

                <q-select outlined  v-model="data.areas" multiple :options="optionsArea" :option-label="opt =>opt.area_name" :label="$t('area')" class="q-mt-sm" @add="val => onChange(val,'add')" @remove="val => onChange(val,'remove')"/>
                <div class="text-center">
                    <q-btn label="Submit" type="submit" color="primary" :loading="loading"/>
                </div>
                </q-form>

                </div>
        <q-card-actions align="right">
          <q-btn flat :label="$t('close')" color="primary" no-caps @click="emit('closeModalLevel')"/>
        </q-card-actions>
        </q-card>
    </q-dialog>
</template>
<style scoped>
</style>