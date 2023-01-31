<script setup>
    import { useQuasar } from 'quasar'
    import axios from 'axios';

    const $q = useQuasar()
    const props = defineProps({
        title:{
            type:String,
            required:true
        },
        nameToDelete:{
            type:String,
            required:true
        },
        data:{
            type:Object,
            required:true
        },
        showModalDelete:{
            type:Boolean,
            required:true,
            default:false
        }
    })
    
    const emit = defineEmits(['closeModalDelete'])
    const SendDelete = ()=>{
        axios.delete(props.data.url)
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
        .finally(()=>emit('closeModalDelete'))
    }
</script>
<template>

    <q-dialog v-model="showModalDelete">
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="warning" color="red" text-color="white" />
          <span class="q-ml-sm">{{$t(title,{name:nameToDelete})}}</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancelar" color="primary" no-caps @click="emit('closeModalDelete')"/>
          <q-btn  label="Sí, eliminar" color="red" no-caps @click="SendDelete"/>
        </q-card-actions>
      </q-card>
    </q-dialog>

</template>