<script setup>
import { ref } from 'vue'
import { useStorePositionsDetails } from '@/store/vacancies/positionsDetails.js'
import CreateVacancieModal from '@/components/admin/utilities/CreateVacancieModal.vue'
import Cards from '@/components/public/Cards.vue'
import DeleteModal from '@/components/admin/utilities/DeleteModal.vue'


    const columns = [
                        {
                            name: 'nivel',
                            required: true,
                            label: 'Nivel',
                            align: 'left',
                            // field: row => row.name,
                            // format: val => `${val}`,
                            sortable: true
                        },
                        { name: 'area', align: 'left', label: 'Área', field: 'area', sortable: true },
                        { name: 'denominacion', align: 'left',label: 'Denominación', field: 'denominacion', sortable: true, style: 'width: 10px' },
                        { name: 'dateCreation', align: 'left',label: 'Fecha de creación', field: 'dateCreation' },
                        { name: 'active', align: 'left',label: 'Activo', field: 'active' },
                        { name: 'actions', align: 'cebter',label: 'Acciones', field: 'actions' }
                    ]
    const storeVacancies = useStorePositionsDetails()
    const rows = ref(storeVacancies.positions)
    const dataVacancie = ref(
      {
               denominacion: '',
               area:[],
               nivel:[],
               active:true,
               dateCreation:`${new Date().getFullYear()}/${new Date().getMonth()+1}/${new Date().getDate()}`,
               description: '',
               years_of_experience: 0,
               positionImmediateSuperior:'',
               dateOfEntry:null,
               aditionalKnowledge:'',
               competencies:[],
               experience_description: '',
               languages: '',
               laboralConditions:[],
               purpose: '',
               responsabilities: [],
               internal_relations_contacts: [],//{id: 1, name: 'Estudiantes'}
               internal_relations_objetives: [],//{id: 1, description: 'Brindar apoyo en procesos acádemicos y psicológicos.'}
               external_relations_contacts: [],//{id: 1, name: 'Psicológos'}
               external_relations_objetives: [],//{id: 3, description: 'Remitir procesos y mantener comunicación con los especialistas externos con el fin de realizar un trabajo interdisciplinario.'}
               academic: []//{id: 4, name: 'Profesional', desc: 'Psicología'}
              }
    )
    const showModalVacancies = ref(false)
    const closeModalVacancies = ()=> {
      dataVacancie.value = {
               denominacion: '',
               area:[],
               nivel:[],
               active:true,
               dateCreation:`${new Date().getFullYear()}/${new Date().getMonth()+1}/${new Date().getDate()}`,
               description: '',
               years_of_experience: 0,
               positionImmediateSuperior:'',
               dateOfEntry:null,
               aditionalKnowledge:'',
               competencies:[],
               experience_description: '',
               languages: '',
               laboralConditions:[],
               purpose: '',
               responsabilities: [],
               internal_relations_contacts: [],//{id: 1, name: 'Estudiantes'}
               internal_relations_objetives: [],//{id: 1, description: 'Brindar apoyo en procesos acádemicos y psicológicos.'}
               external_relations_contacts: [],//{id: 1, name: 'Psicológos'}
               external_relations_objetives: [],//{id: 3, description: 'Remitir procesos y mantener comunicación con los especialistas externos con el fin de realizar un trabajo interdisciplinario.'}
               academic: []//{id: 4, name: 'Profesional', desc: 'Psicología'}
              }
      showModalVacancies.value = false
    }
    const showModalDelete = ref(false)
    const dataToDelete = ref(null)
    const openModalToDelete = (data)=>{
      dataToDelete.value = data
      showModalDelete.value = true
    }
    const deleteVacancie = ()=>{
      storeVacancies.deleteVacancie(dataToDelete.value)
      dataToDelete.value = null
      showModalDelete.value = false
    }
    const editVacancie = (data)=>{
      dataVacancie.value = data
      showModalVacancies.value = true
    }
    
</script>
<template>
    
    <div class="q-pa-md">
      <q-table
        title="Vacantes"
        :dense="$q.screen.lt.md"
        :rows="rows"
        :columns="columns"
        row-key="name"
        binary-state-sort
      >
        <template v-slot:top>
            <span><b>Vacantes</b></span>
            <q-space />
            <!-- <q-btn @click="openModalCreateVacancie" color="primary" icon="add" label="Nueva vacante"/> -->
            <q-btn @click="showModalVacancies = true" color="primary" icon="add" :label="$t('newVacancie')" no-caps/>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="nivel" :props="props">
              {{ `${props.row.nivel ? props.row.nivel.map(x=>x.name):''}` }}
            </q-td>
            <q-td key="area" :props="props">
              {{  `${props.row.area ? props.row.area.map(x=>x.name):''}`}}
            </q-td>
            <q-td key="denominacion" :props="props">
              <div class="text-pre-wrap">{{ props.row.denominacion }}</div>
              <q-popup-edit v-model="props.row.denominacion" v-slot="scope">
                <q-input type="textarea" v-model="scope.value" dense autofocus />
              </q-popup-edit>
            </q-td>
            <q-td key="dateCreation" :props="props">{{ props.row.dateCreation }}</q-td>
            <q-td key="active" :props="props">{{ props.row.active }}</q-td>
            <q-td key="actions" :props="props" >
                <div class="q-gutter-sm">
                    <q-btn color="blue" icon="edit" @click="editVacancie(props.row)">
                      <q-tooltip class="bg-blue" :offset="[10, -50]">
                        Editar
                      </q-tooltip>
                    </q-btn>
                    <q-btn color="red"  icon="delete" @click="openModalToDelete(props.row)">
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
    <!-- <DeleteModal/> -->
    <div v-if="showModalVacancies">
      <CreateVacancieModal :vacancieData="dataVacancie" :showModalVacancies="showModalVacancies" @closeModalVacancies="closeModalVacancies"></CreateVacancieModal>
    </div>

    <Cards></Cards>
  </template>