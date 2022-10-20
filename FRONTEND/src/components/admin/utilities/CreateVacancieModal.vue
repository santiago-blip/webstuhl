<script setup>
import { ref } from 'vue';
import {useStorePositionsDetails} from '@/store/vacancies/positionsDetails.js'
    //Mostrar modal y funciones de steppers y tabs.
    const step = ref(1)
    const tab = ref('es')
    //Datos del store y configuración de la estructura de la vacante.
    const storePositions = useStorePositionsDetails()
    const emit = defineEmits(['closeModalVacancies'])
    const props = defineProps({
        showModalVacancies:{
            type:Boolean,
            default:false
        },
        vacancieData :{ 
            type:Object
            }
    })
    const vacancie = ref(props.vacancieData)
    const responsabilitie = ref('')
    const competencie = ref('')
    const laboralCondition = ref('')
    //Funciones para agregar/remover las responsabilidades y competencias. condition = 1: Trabaja responsabilidades.
    //condition = 2: Trabaja competencias.
    const addAttribute = (condition = 1)=>{
        let value = condition == 1 ?responsabilitie.value.trim():condition == 2?competencie.value.trim():laboralCondition.value.trim()
        if(value && !vacancie.value.responsabilities.find(x=>x==value) && condition == 1){
            vacancie.value.responsabilities.push(value)
            responsabilitie.value = ''
            return
        }
        if(value && !vacancie.value.competencies.find(x=>x==value) && condition == 2){
            vacancie.value.competencies.push(value)
            competencie.value = ''
            return
        }
        if(value && !vacancie.value.laboralConditions.find(x=>x==value) && condition == 3){
            vacancie.value.laboralConditions.push(value)
            laboralCondition.value = ''
            return
        }
    }
    const removeResponsabilitie = (data,condition = 1)=>{
        if(condition == 1){
            vacancie.value.responsabilities.splice(vacancie.value.responsabilities.indexOf(data),1)
            return
        }
        if(condition == 2){
            vacancie.value.competencies.splice(vacancie.value.competencies.indexOf(data),1)
            return
        }
        if(condition == 3){
            vacancie.value.laboralConditions.splice(vacancie.value.laboralConditions.indexOf(data),1)
            return
        }
    }

    //Registrar vacante
    const finishedStepper = ()=>{
        step.value = 1
        storePositions.addVacancie(vacancie.value)
        vacancie.value = {
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
        emit('closeModalVacancies')
    }

    //Cambiar los datos del datepicker al español.
    const myLocaleDates = {
        /* starting with Sunday */
        days: 'Domingo_Lunes_Martes_Miércoles_Jueves_Viernes_Sábado'.split('_'),
        daysShort: 'Dom_Lun_Mar_Mié_Jue_Vie_Sáb'.split('_'),
        months: 'Enero_Febrero_Marzo_Abril_Mayo_Junio_Julio_Agosto_Septiembre_Octubre_Noviembre_Diciembre'.split('_'),
        monthsShort: 'Ene_Feb_Mar_Abr_May_Jun_Jul_Ago_Sep_Oct_Nov_Dic'.split('_'),
        format24h: true,
        pluralDay: 'dias'
      }

    // const checkVacancie = ()=>console.log(vacancie.value)//TEMP
</script>
<template>
    
    <q-dialog v-model="showModalVacancies" persistent full-width>
                <q-card>
                <q-tabs
                v-model="tab"
                dense
                class="text-grey"
                active-color="primary"
                indicator-color="primary"
                align="justify"
                narrow-indicator
                >
                <q-tab name="es" label="Español" />
                <q-tab name="en" label="Inglés" />
                </q-tabs>
                
                <q-separator />

                <q-tab-panels v-model="tab" animated>
                <q-tab-panel name="es">
                    <q-stepper
                        v-model="step"
                        ref="stepper"
                        animated
                        >
                        <q-step
                            :name="1"
                            title="Datos de identificación del cargo"
                            icon="settings"
                            :done="step > 1"
                        >
                        <div class="row">
                            <div class="col-5 q-px-xs">
                                <q-input  outlined  v-model="vacancie.denominacion" autogrow label="Denominación" class="q-mt-sm"/>
                                <q-select outlined  v-model="vacancie.nivel" clearable multiple :options="storePositions.level" :option-label="opt => opt.name" label="Nivel" class="q-mt-sm"/>
                                <q-select outlined  v-model="vacancie.area" clearable multiple :options="storePositions.area" :option-label="opt => opt.name" label="Área" class="q-mt-sm"/>
                                <q-input  outlined  v-model="vacancie.positionImmediateSuperior" autogrow label="Cargo del jefe inmediato" class="q-mt-sm"/>
                                <q-input  outlined  v-model="vacancie.purpose" autogrow label="Proposito" class="q-mt-sm"/>
                                <q-toggle v-model="vacancie.active" :color="`${vacancie.active?'green':'red'}`" :label="`La vacante está: ${vacancie.active?'activa':'desactivada'}`" />
                            </div>
                            <div class="col-4 q-px-xs">
                                <q-input  @keydown.enter="addAttribute()" v-model="responsabilitie" outlined  autogrow label="Responsabilidades" class="q-mt-sm"/>
                                <q-scroll-area class="q-scroll-area-comp" v-if="vacancie.responsabilities?.length" style="height: 150px;">
                                    <ul class="ul-list-responsabilities">
                                        <li v-for="(res,index) in vacancie.responsabilities" :key="index">
                                        <div>
                                            {{res}}
                                            <q-icon name="close" style="font-size: 1.4em;cursor: pointer;" @click="removeResponsabilitie(res)" size="xs" color="red"/>
                                            <!-- <q-btn color="red" icon="close"  @click="removeResponsabilitie(res)" size="xs"/> -->
                                        </div>
                                        </li>
                                    </ul>
                                </q-scroll-area>
                            </div>
                            <div class="col-3 q-px-xs text-center">
                                <label>Fecha de ingreso</label>
                                <div class="q-pa-md" style="display:flex; justify-content: center;">
                                    <q-date  v-model="vacancie.dateOfEntry" :locale="myLocaleDates"/>
                                </div>
                            </div>
                        </div>
                        </q-step>
                        <q-step
                            :name="2"
                            title="Formación y certificaciones"
                            icon="create_new_folder"
                            :done="step > 2"
                        >
                            <div class="row">
                                <div class="col-6 q-px-xs">
                                    <q-select outlined  v-model="vacancie.academic" clearable multiple :options="storePositions.profession" :option-label="opt => opt.name" label="Nivel académico" class="q-mt-sm"/>
                                    <q-input  outlined  v-model="vacancie.languages" autogrow label="Idiomas" class="q-mt-sm"/>
                                    <q-input  outlined  v-model="vacancie.aditionalKnowledge" autogrow label="Conocimiento adicional" class="q-mt-sm"/> 
                                    </div>
                                <div class="col-6 q-px-xs">
                                    <q-input  @keydown.enter="addAttribute(2)" v-model="competencie" outlined  autogrow label="Competencias" class="q-mt-sm"/>
                                    <q-scroll-area class="q-scroll-area" v-if="vacancie.competencies?.length" style="height: 150px;">
                                        <ul class="ul-list-responsabilities">
                                            <li v-for="(res,index) in vacancie.competencies" :key="index">
                                            <div>
                                                {{res}}
                                                <q-icon name="close" style="font-size: 1.4em;cursor: pointer;" @click="removeResponsabilitie(res,2)" size="xs" color="red"/>
                                                <!-- <q-btn color="red" icon="close"  @click="removeResponsabilitie(res)" size="xs"/> -->
                                            </div>
                                            </li>
                                        </ul>
                                    </q-scroll-area>
                                </div>
                            </div>
                        </q-step>
                        <q-step
                            :name="3"
                            title="Experiencia, relaciones y condiciones"
                            icon="assignment"
                            :done="step > 3"
                        >
                            <div class="row">
                                <div class="col-3 q-px-xs">
                                    <q-input  outlined  type="number" v-model.number="vacancie.years_of_experience" label="Años de experiencia" class="q-mt-sm"/>                                   
                                    <q-input  outlined  v-model="vacancie.experience_description" autogrow label="Áreas y procesos" class="q-mt-sm"/> 
                                </div>
                                <div class="col-3 q-px-xs">
                                    <q-select outlined  v-model="vacancie.internal_relations_contacts" clearable multiple :options="storePositions.internal_contacts" :option-label="opt => opt.name" label="Relaciones internas" class="q-mt-sm"/>
                                    <q-select outlined  v-model="vacancie.external_relations_contacts" clearable multiple :options="storePositions.external_contacts" :option-label="opt => opt.name" label="Relaciones externas" class="q-mt-sm"/>
                                </div>
                                <div class="col-3 q-px-xs">
                                    <q-select outlined  v-model="vacancie.internal_relations_objetives" clearable multiple :options="storePositions.relations_objetives" :option-label="opt => opt.description" label="Objetivos de las relaciones internas" class="q-mt-sm"/>
                                    <q-select outlined  v-model="vacancie.external_relations_objetives" clearable multiple :options="storePositions.relations_objetives" :option-label="opt => opt.description" label="Objetivos de las relaciones externas" class="q-mt-sm"/>
                                </div>
                                <div class="col-3 q-px-xs">
                                    <q-input  @keydown.enter="addAttribute(3)" v-model="laboralCondition" outlined  autogrow label="Condiciones laborales" class="q-mt-sm"/>
                                    <q-scroll-area class="q-scroll-area" v-if="vacancie.laboralConditions?.length" style="height: 150px;">
                                        <ul class="ul-list-responsabilities">
                                            <li v-for="(res,index) in vacancie.laboralConditions" :key="index">
                                            <div>
                                                {{res}}
                                                <q-icon name="close" style="font-size: 1.4em;cursor: pointer;" @click="removeResponsabilitie(res,3)" size="xs" color="red"/>
                                                <!-- <q-btn color="red" icon="close"  @click="removeResponsabilitie(res)" size="xs"/> -->
                                            </div>
                                            </li>
                                        </ul>
                                    </q-scroll-area>
                                </div>
                            </div>
                        </q-step>
                        <q-step
                            :name="4"
                            title="Create an ad"
                            icon="add_comment"
                            :done="step > 4"
                        >
                            Presiona finalizar para registrar la vacante.
                        </q-step>

                        <template v-slot:navigation>
                            <q-stepper-navigation>
                            <q-btn v-if="step < 4" @click="$refs.stepper.next()" color="primary" label="Siguiente" no-caps/>
                            <q-btn v-else  color="primary" label="Finalizar" @click="finishedStepper" />
                            <q-btn v-if="step > 1" flat color="primary" @click="$refs.stepper.previous()" label="Volver" class="q-ml-sm" no-caps/>
                            
                            <q-btn color="red"  class="q-ml-sm" icon="close" label="Cerrar" @click="emit('closeModalVacancies')" no-caps/>
                            <!-- <q-btn color="green" @click="checkVacancie" class="q-ml-sm" icon="check" label="Checkear" no-caps/> -->
                            </q-stepper-navigation>
                        </template>
                        </q-stepper>
                </q-tab-panel>

                <q-tab-panel name="en">
                    <div class="text-h6">Alarms</div>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                </q-tab-panel>
                </q-tab-panels>
            </q-card>
    </q-dialog>
</template>
<style scoped>
    .q-scroll-area{
        height: calc(100% - 150px);
        margin-top: 10px;
        /* border-right: 1px solid #ddd; */
    }
    .ul-list-responsabilities{
        word-wrap: break-word;
    }
</style>