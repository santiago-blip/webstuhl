<script setup>
  import { ref,onMounted } from 'vue'
  import { useQuasar } from 'quasar'
  import axios from 'axios'
  import DeleteModal from '@/components/admin/utilities/DeleteModal.vue'
  import ModalCreateLanguage from '@/components/admin/utilities/CreateLanguageModal.vue'
  const $q = useQuasar()
  const columns = [
                        {name: 'language_id',label: 'id',align: 'left',sortable: true},
                        {name: 'language_name',label: 'Lenguaje',align: 'left',sortable: true},
                        {name: 'language_level',label: 'Niveles',align: 'left',sortable: true},
                        { name: 'actions', align: 'cebter',label: 'Acciones', field: 'actions' }
                    ]
  const rows = ref([])
  const loading = ref(false)
  const pagination = {
        rowsPerPage: 10
      }
  const showModalNewLanguage = ref(false)
  const optionsLanguage = ref([])
  const getData = ()=>{
  loading.value = true
  // if(!areaStore.getAllAreas.length){}
    axios.get('http://127.0.0.1:8000/vacancies/master/languages/')
    .then(response=>{
      rows.value = response.data.response
      console.log(rows.value)
      rows.value.forEach(x=>{
        x.levels = x.levels.map(x=>x.language_level)
      })
      console.log(rows.value)
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
  }
  const getDataLevels = ()=>{
  loading.value = true
  // if(!areaStore.getAllAreas.length){}
    axios.get('http://127.0.0.1:8000/vacancies/master/languages-level/')
    .then(response=>{
      optionsLanguage.value = response.data.response
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
  }
  onMounted(() => {
    getData()
    getDataLevels()
  })
  const languageData = ref({language_name:""})
  
  const showModalDelete = ref(false)
  const openModalNewLanguage = ()=>{
    showModalNewLanguage.value = true
  }
  const closeModalNewLanguage = ()=> showModalNewLanguage.value = false
  const cleanData = ()=>{
    languageData.value = {language_name:""}
    getData()
  }
  const submittedData = ()=>{
    cleanData()
    closeModalNewLanguage()
  }

  const updateData = (data)=>{
    languageData.value = data
    openModalNewLanguage()
  }
  const titleDelete = 'deleteLanguage'
  const nameToDelete = ref('')
  const openDeleteModal = (data)=>{
    nameToDelete.value = data.language_name
    languageData.value = data
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
        row-key="name"
        binary-state-sort
      >
        <template v-slot:top>
            <span><b>{{$t('languages')}}</b></span>
            <q-space />
            <!-- <q-btn @click="openModalCreateVacancie" color="primary" icon="add" label="Nueva vacante"/> -->
            <q-btn @click="openModalNewLanguage" color="primary" icon="add" :label="$t('newLanguage')" no-caps/>
            <div v-if="showModalNewLanguage">
              <ModalCreateLanguage :optionsLanguage="optionsLanguage" :languageData="languageData" :showModalNewLanguage="showModalNewLanguage" @closeModalNewLanguage="closeModalNewLanguage" @submittedData="submittedData"/>
            </div>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="language_id" :props="props" >
              {{props.row.id}}
            </q-td>
            <q-td key="language_name" :props="props" >
              {{props.row.language_name}}
            </q-td>
            <q-td key="language_level" :props="props" >
              {{`${props.row.levels.map(x=>x.language_level)}`}}
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
  <DeleteModal :showModalDelete="showModalDelete" :nameToDelete="nameToDelete" :title="titleDelete" :data="languageData" @closeModalDelete="closeDeleteModal"/>
</div>
  </template>