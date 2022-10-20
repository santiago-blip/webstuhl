<script setup>
    /*
      imports
    */
   
    import { useStorePositionsDetails } from '@/store/vacancies/positionsDetails'
    import { useRoute } from 'vue-router'
    import VacancieDescription from '@/components/public/VacancieDescription.vue'
    import VacancieAcademicAndCert from '@/components/public/VacancieAcademicAndCert.vue'
    import VacancieExperienceRelationsConditions from '@/components/public/VacancieExperienceRelationsConditions.vue'
    
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
            <q-toolbar-title class="text-weight-bold">Fechas y contacto</q-toolbar-title>
            </q-toolbar>
            <q-list>
                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Fecha de ingreso</q-item-label>
                    <q-item-label> {{ storePositions.getPositionsContent($route.params.id).dateOfEntry }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Contacto</q-item-label>
                    <q-item-label> vacancies@columbus.edu.co</q-item-label>
                    </q-item-section>
                </q-item>
            </q-list>
</template>