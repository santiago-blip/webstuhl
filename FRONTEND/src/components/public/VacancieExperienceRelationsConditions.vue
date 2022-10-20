<script setup>
    /*
      imports
    */
   
    import { useStorePositionsDetails } from '@/store/vacancies/positionsDetails'
    import { useRoute } from 'vue-router'
   
    
    /*
    store
    */
    const storePositions = useStorePositionsDetails()

    /*
    router
    */
    const route = useRoute
    

</script>


<template>
     <q-toolbar class="bg-primary text-white shadow-2">
            <q-toolbar-title class="text-weight-bold">Experiencia, Relaciones y Condiciones</q-toolbar-title>
            </q-toolbar>
            <q-list>
                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Años de Experiencia</q-item-label>
                    <q-item-label> {{ storePositions.getPositionsContent($route.params.id).years_of_experience }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Areás o Procesos</q-item-label>
                    <q-item-label> {{ storePositions.getPositionsContent($route.params.id).experience_description }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Relaciones Internas</q-item-label>
                    <q-item-label> {{ `${storePositions.getPositionsContent($route.params.id).internal_relations_contacts.map(x=>x.name)}` }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Objetivos Relaciones Internas</q-item-label>
                    <q-item-label> {{ `${storePositions.getPositionsContent($route.params.id).internal_relations_objetives.map(x=>x.description)}` }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Relaciones Externas</q-item-label>
                    <q-item-label> {{ `${storePositions.getPositionsContent($route.params.id).external_relations_contacts.map(x=>x.name)}` }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Objetivos Relaciones Internas</q-item-label>
                    <q-item-label> {{ `${storePositions.getPositionsContent($route.params.id).external_relations_objetives.map(x=>x.description)}` }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Condiciones Laborales</q-item-label>
                    <q-item-label> {{ `${storePositions.getPositionsContent($route.params.id).laboralConditions.map(x=>x)}` }}</q-item-label>
                    </q-item-section>
                </q-item>

            </q-list>
</template>