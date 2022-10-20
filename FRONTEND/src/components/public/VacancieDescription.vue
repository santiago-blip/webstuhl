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
            <q-toolbar-title class="text-weight-bold">Descripción</q-toolbar-title>
            </q-toolbar>
            <q-list>
                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Denominación</q-item-label>
                    <q-item-label> {{ storePositions.getPositionsContent($route.params.id).denominacion }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Nivel</q-item-label>
                    <q-item-label> {{ `${storePositions.getPositionsContent($route.params.id).nivel.map(x=>x.name)}` }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Areá</q-item-label>
                    <q-item-label> {{ `${storePositions.getPositionsContent($route.params.id).area.map(x=>x.name)}` }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Cargo Jefe Inmediato</q-item-label>
                    <q-item-label> {{ storePositions.getPositionsContent($route.params.id).positionImmediateSuperior }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item>
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Propósito</q-item-label>
                    <q-item-label> {{ storePositions.getPositionsContent($route.params.id).purpose }}</q-item-label>
                    </q-item-section>
                </q-item>

                <q-separator spaced inset />

                <q-item class="q-mb-sm">
                    <q-item-section>
                    <q-item-label class="text-weight-bold">Responsabilidades</q-item-label>
                    <q-item
                    v-for="(responsability, index) in storePositions.getPositionsContent($route.params.id).responsabilities"
                    :key="index"
                    >
                {{ '•' }} {{ responsability }}
                </q-item>
                    <!--<q-item-label
                    > {{ `${storePositions.getPositionsContent($route.params.id).responsabilities.map(x=>x)}` }}</q-item-label>-->
                    </q-item-section>
                </q-item>


            </q-list>
</template>