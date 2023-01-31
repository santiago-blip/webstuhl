<script setup>
  import { ref } from 'vue'
  import { onMounted } from 'vue'
  import { useQuasar } from 'quasar'
  import axios from 'axios'
  import ModalCreateLevel from '@/components/admin/utilities/CreateLevelModal.vue'
  import DeleteModal from '@/components/admin/utilities/DeleteModal.vue'
  import AreaStore from '../../../store/masters/areasStore.js'

  const $q = useQuasar()
  const columns = [
                        { name: 'level_id',label: 'Id',align: 'left',sortable: true},
                        { name: 'level_name',label: 'Nombre',align: 'left',sortable: true},
                        { name: 'level_description',label: 'Descripción',align: 'left',sortable: true},
                        { name: 'areas_relations',label: 'Áreas relacionadas',align: 'left',sortable: true},
                        { name: 'actions', align: 'cebter',label: 'Acciones', field: 'actions' }
                    ]
  const rows = ref([])
  const loading = ref(false)
  const pagination = {
        rowsPerPage: 10
      }
  
  const optionsArea = ref([])
// const areaStore = AreaStore()

  const getDataArea = ()=>{
    loading.value = true
      axios.get('http://127.0.0.1:8000/vacancies/master/areas/')
      .then(response=>{
        optionsArea.value = response.data.response
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
  }


const getData = ()=>{
  loading.value = true
  // axios.get('http://127.0.0.1:8000/vacancies/master/levels/')
  axios.get('http://127.0.0.1:8000/vacancies/master/levels-relations-areas/')
   .then(response=>{
    rows.value = response.data.response
    rows.value.forEach(x=>{
      x.areas = x.areas.map(y=>y.area_id)
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
   .finally(()=>loading.value = false)
}
  onMounted(() => {
    getData()
    getDataArea()
  })
  const levelData = ref({
    level_name:"",
    level_description:""
  })
  const showModalNewLevel = ref(false)
  const showModalDelete = ref(false)
  const openModalNewLevel = ()=>{
    showModalNewLevel.value = true
  }
  const closeModalNewlevel = ()=> showModalNewLevel.value = false
  const cleanData = ()=>{
    levelData.value = {level_name:"",level_description:""}
    getData()
  }
  const submittedData = ()=>{
    cleanData()
    closeModalNewlevel()
  }

  const updateData = (data)=>{
    levelData.value = Object.assign(data)
    openModalNewLevel()
  }
  const titleDelete = 'deleteLevel'
  const nameToDelete = ref('')
  const openDeleteModal = (data)=>{
    levelData.value = data
    nameToDelete.value = data.level_name
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
            <span><b>{{$t('level')}}</b></span>
            <q-space />
            <!-- <q-btn @click="openModalCreateVacancie" color="primary" icon="add" label="Nueva vacante"/> -->
            <q-btn @click="openModalNewLevel" color="primary" icon="add" :label="$t('newLevel')" no-caps/>
            <div v-if="showModalNewLevel">
              <ModalCreateLevel :optionsArea="optionsArea" :levelData="levelData" :showModalNewLevel="showModalNewLevel" @closeModalLevel="closeModalNewlevel" @submittedData="submittedData"/>
            </div>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="level_id" :props="props">
              {{props.row.id}}
            </q-td>
            <q-td key="level_name" :props="props">
              {{props.row.level_name}}
            </q-td>
            <q-td key="level_description" :props="props">
              {{props.row.level_description}}
            </q-td>
            <q-td key="areas_relations" :props="props">
              {{`${props.row.areas.map(data=>data.area_name)}`}}
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
  <DeleteModal :showModalDelete="showModalDelete" :nameToDelete="nameToDelete" :title="titleDelete" :data="levelData" @closeModalDelete="closeDeleteModal"/>
</div>
  </template>