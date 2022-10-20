<script setup>
    /*
      imports
    */
   
    import { useStorePositionsDetails } from '@/store/vacancies/positionsDetails'
    
    /*
    store
    */
    const storePositions = useStorePositionsDetails()
    

</script>

<template>

    <div class="row justify-center q-mt-lg q-gutter-lg">

    
    <div
    v-for="position in storePositions.positions"
            :key="position.id"
            :position="position"

    >

    
        
    <q-card v-if="position.active">
      <q-card-section class="bg-primary text-white">
        <div class="text-h6 text-weight-bold">{{ position.denominacion }}</div>
      </q-card-section>

      <q-separator />

      <q-list>
        <div class="text-h6 q-pl-sm q-mt-sm q-mb-xs">Perfil:</div>
        <q-item clickable>
          <q-item-section avatar>
            <q-icon color="primary" name="badge" />
          </q-item-section>
        <q-item-section>
            <q-item-label class="text-h5">{{ `${position.academic.map(x=>x.name)}` }}</q-item-label>
            <q-item-label caption>Psiquiatría basica</q-item-label>
          </q-item-section>
        </q-item>

        <div class="text-h6 q-pl-sm q-mt-sm q-mb-xs">Idiomas:</div>
        <q-item clickable>
          <q-item-section avatar>
            <q-icon color="primary" name="translate" />
          </q-item-section>
        <q-item-section>
            <q-item-label class="text-h5">{{ position.languages }}</q-item-label>
            <q-item-label caption>Niveles Según el Marco Común Europeo</q-item-label>
          </q-item-section>
        </q-item>

        <div class="text-h6 q-pl-sm q-mt-sm q-mb-xs">Experiencia</div>
        <q-item clickable>
          <q-item-section avatar>
            <q-icon color="primary" name="work" />
          </q-item-section>
        <q-item-section>
            <q-item-label class="text-h5">{{ position.years_of_experience }} años</q-item-label>
            <q-item-label caption>{{ position.experience_description }}</q-item-label>
          </q-item-section>
        </q-item>

    </q-list>

      <q-card-actions align="center" class="q-my-sm">
        <div>
        <q-btn 
        @click="$router.push({name:'details',params:{id:position.id}})"
        color="primary"
        no-caps="">Ver Detalle</q-btn>  
        </div>
      </q-card-actions>
    
    </q-card>
  </div>
</div>


</template>


<style scoped>
    .vacancie-card {
      width: 100%;
      max-width: 350px;
    }
</style>