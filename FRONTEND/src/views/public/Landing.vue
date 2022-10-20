<script setup>
 /*
imports
*/
import NavbarLanding from '@/components/public/NavbarLanding.vue'
import Cards from '@/components/public/Cards.vue'
import { useStorePositionsDetails } from '@/store/vacancies/positionsDetails'
import FooterLanding from '@/components/public/FooterLanding.vue'
    
 /*
store
*/
    
const storePositions = useStorePositionsDetails()
</script>



<template>

<q-layout>

      
      <NavbarLanding></NavbarLanding>
      
      <div align="center">
      <img src="https://www.columbus.edu.co/wp-content/uploads/Columbus-logo.png" alt="">
     </div>
         

      <q-page-container>
         <Cards></Cards>
      </q-page-container>


      <q-footer>
        <FooterLanding></FooterLanding>
      </q-footer>

</q-layout>
     
</template>