<script setup>
  import { ref } from 'vue'
  import { onMounted } from 'vue'
  import { useQuasar } from 'quasar'
  import axios from 'axios'
  import ModalCreateProfession from '@/components/admin/utilities/CreateProfessionModal.vue'
  import DeleteModal from '@/components/admin/utilities/DeleteModal.vue'
  import AreaStore from '../../../store/masters/areasStore.js'

  const areaStore = AreaStore()
  const $q = useQuasar()
  const columns = [
                        { name: 'profession_id',label: 'Id',align: 'left',sortable: true},
                        { name: 'profession_name',label: 'Nombre',align: 'left',sortable: true},
                        { name: 'actions', align: 'cebter',label: 'Acciones', field: 'actions' }
                    ]
  const rows = ref([])
  const loading = ref(false)
  const pagination = {
        rowsPerPage: 10
      }
  
const getData = ()=>{
  loading.value = true
  // if(!areaStore.getAllAreas.length){}
    axios.get('http://127.0.0.1:8000/vacancies/master/professions/')
    .then(response=>{
      rows.value = response.data.response
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
    .finally(()=>loading.value = false)
  // rows.value = areaStore.getAllAreas
  // loading.value = false
  
}
  onMounted(() => {
    getData()
  })
  const professionData = ref({
    profession_name:"",
  })
  const showModalNewProfession = ref(false)
  const showModalDelete = ref(false)
  const openModalNewProfession = ()=>{
    showModalNewProfession.value = true
  }
  const closeModalNewProfession = ()=> showModalNewProfession.value = false
  const cleanData = ()=>{
    professionData.value = {profession_name:""}
    getData()
  }
  const submittedData = ()=>{
    cleanData()
    closeModalNewProfession()
  }

  const updateData = (data)=>{
    professionData.value = data
    openModalNewProfession()
  }
  const titleDelete = 'deleteProfession'
  const nameToDelete = ref('')
  const openDeleteModal = (data)=>{
    nameToDelete.value = data.profession_name
    professionData.value = data
    showModalDelete.value = true
  }
  const closeDeleteModal = ()=>{
    showModalDelete.value = false
    cleanData()
  }

</script>
<template>
    
    <div class="q-pa-md">
      <q-table
        
        :dense="$q.screen.lt.md"
        :rows="rows"
        :columns="columns"
        :pagination.sync="pagination"
        row-key="name"
        binary-state-sort
        :loading="loading"
      >
      <template v-slot:loading>
        <q-inner-loading showing color="primary" />
      </template>
        <template v-slot:top>
            <span><b>{{$t('profession')}}</b></span>
            <q-space />
            <!-- <q-btn @click="openModalCreateVacancie" color="primary" icon="add" label="Nueva vacante"/> -->
            <q-btn @click="openModalNewProfession" color="primary" icon="add" :label="$t('newProfession')" no-caps/>
            <div v-if="showModalNewProfession">
              <ModalCreateProfession :professionData="professionData" :showModalNewProfession="showModalNewProfession" @closeModalProfession="closeModalNewProfession" @submittedData="submittedData"/>
            </div>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="profession_id" :props="props">
              {{props.row.id}}
            </q-td>
            <q-td key="profession_name" :props="props">
              {{props.row.profession_name}}
            </q-td>
            <q-td key="actions" :props="props" >
                <div class="q-gutter-sm">
                    <q-btn color="blue" icon="edit" @click="updateData(props.row)">
                      <q-tooltip class="bg-blue" :offset="[10, -50]">
                        Editar
                      </q-tooltip>
                    </q-btn>
                    <q-btn color="red"  icon="delete" @click="openDeleteModal(props.row)">
                      <q-tooltip class="bg-red" :offset="[10, -50]">
                        Eliminar
                      </q-tooltip> 
                    </q-btn>
                </div>
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </div>
<div v-if="showModalDelete">
  <DeleteModal :showModalDelete="showModalDelete" :nameToDelete="nameToDelete" :title="titleDelete" :data="professionData" @closeModalDelete="closeDeleteModal"/>
</div>
  </template>