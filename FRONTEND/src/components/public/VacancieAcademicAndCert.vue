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
            <q-toolbar-title class="text-weight-bold">Formación Academica y Certificaciones</q-toolbar-title>
            </q-toolbar>
            <q-list>
                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Nivel Educativo</q-item-label>
                    <q-item-label> {{ `${storePositions.getPositionsContent($route.params.id).academic.map(x=>x.name)}` }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Idiomas</q-item-label>
                    <q-item-label> {{ storePositions.getPositionsContent($route.params.id).languages }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Conocimientos Adicionales</q-item-label>
                    <q-item-label> {{ storePositions.getPositionsContent($route.params.id).aditionalKnowledge }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Competencias</q-item-label>
                    <q-item-label> {{ `${storePositions.getPositionsContent($route.params.id).competencies.map(x=>x)}` }}</q-item-label>
                    </q-item-section>
                </q-item>

            </q-list>
</template>