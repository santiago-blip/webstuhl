<script setup>
  import { ref,onMounted } from 'vue'
  import { useQuasar } from 'quasar'
  import axios from 'axios'
  import DeleteModal from '@/components/admin/utilities/DeleteModal.vue'
  import ModalCreateInternalContactObjetive from '@/components/admin/utilities/CreateInternalContactObjetiveModal.vue'
  const $q = useQuasar()
  const columns = [
                        {name: 'Internal_relations_objetives_id',label: 'id',align: 'center',sortable: true},
                        {name: 'Internal_relations_objetives_name',label: 'Nombre',align: 'center',sortable: true},
                        { name: 'actions', align: 'center',label: 'Acciones', field: 'actions' }
                    ]
  const rows = ref([])
  const loading = ref(false)
  const pagination = {
        rowsPerPage: 10
      }
  const showModalNewInternalContact = ref(false)
  const getData = ()=>{
  loading.value = true
  // if(!areaStore.getAllAreas.length){}
    axios.get('http://127.0.0.1:8000/vacancies/master/internalRelationsObjetives/')
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
  }
  onMounted(() => {
    getData()
  })
  const internalContactData = ref({Internal_relations_objetives_name:""})
  
  const showModalDelete = ref(false)
  const openModalNewInternalContact = ()=>{
    showModalNewInternalContact.value = true
  }
  const closeModalNewInternalContact = ()=> showModalNewInternalContact.value = false
  const cleanData = ()=>{
    internalContactData.value = {Internal_relations_objetives_name:""}
    getData()
  }
  const submittedData = ()=>{
    cleanData()
    closeModalNewInternalContact()
  }

  const updateData = (data)=>{
    internalContactData.value = data
    openModalNewInternalContact()
  }
  const titleDelete = 'deleteInternalObjetivesContact'
  const nameToDelete = ref('')
  const openDeleteModal = (data)=>{
    nameToDelete.value = data.Internal_relations_objetives_name
    internalContactData.value = data
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
            <span><b>{{$t('internalContactObjetives')}}</b></span>
            <q-space />
            <!-- <q-btn @click="openModalCreateVacancie" color="primary" icon="add" label="Nueva vacante"/> -->
            <q-btn @click="openModalNewInternalContact" color="primary" icon="add" :label="$t('newInternalContactoObjetives')" no-caps/>
            <div v-if="showModalNewInternalContact">
              <ModalCreateInternalContactObjetive :internalContactData="internalContactData" :showModalNewInternalContact="showModalNewInternalContact" @closeModalNewInternalContact="closeModalNewInternalContact" @submittedData="submittedData"/>
            </div>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="Internal_relations_objetives_id" :props="props" >
              {{props.row.id}}
            </q-td>
            <q-td key="Internal_relations_objetives_name" :props="props" >
              {{props.row.Internal_relations_objetives_name}}
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
  <DeleteModal :showModalDelete="showModalDelete" :nameToDelete="nameToDelete" :title="titleDelete" :data="internalContactData" @closeModalDelete="closeDeleteModal"/>
</div>
  </template>