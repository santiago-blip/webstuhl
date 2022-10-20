<script setup>
    /*
      imports
    */
   
    import { useStorePositionsDetails } from '@/store/vacancies/positionsDetails'
    import { useRoute } from 'vue-router'
    import VacancieDescription from '@/components/public/VacancieDescription.vue'
    import VacancieAcademicAndCert from '@/components/public/VacancieAcademicAndCert.vue'
    import VacancieExperienceRelationsConditions from '@/components/public/VacancieExperienceRelationsConditions.vue'
    import VacancieDatesAndContact from '@/components/public/VacancieDatesAndContact.vue'
    
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
    <q-banner dense class="bg-primary">
        <div align="center" class="text-h5 text-white text-weight-bold">
            {{ storePositions.getPositionsContent($route.params.id).denominacion }}
        </div>
    </q-banner>

    <div class="row justify-center q-gutter-lg q-mt-xs q-mx-md">

        <div class="col-xs-10 col-sm-6 col-md-3" style="border: 1px solid #000; border-radius: 5px;">
            <VacancieDescription></VacancieDescription>
        </div>

        <div class="col-xs-10 col-sm-6 col-md-3" style="border: 1px solid #000; border-radius: 5px;">
            <VacancieExperienceRelationsConditions></VacancieExperienceRelationsConditions>
        </div>

        <div class="col-xs-10 col-sm-6 col-md-3" style="border: 1px solid #000; border-radius: 5px;">
           <VacancieAcademicAndCert></VacancieAcademicAndCert>
        </div>

        <div class="col-9 q-mb-xl" style="border: 1px solid #000; border-radius: 5px;">
            <VacancieDatesAndContact></VacancieDatesAndContact>
        </div>


    </div>

   
</template>