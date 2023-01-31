import {defineStore} from 'pinia'
import axios from 'axios'
import { useQuasar } from 'quasar'

const AreaStore = defineStore('areaStore',{
    state:()=>({
        allAreas:[],
        $q:useQuasar()
    }),
    getters:{
        getAllAreas(state){
            return state.allAreas
        }
    },
    actions:{
        setAreas(){
            axios.get('http://127.0.0.1:8000/vacancies/master/areas/')
            .then(response=>{
                this.allAreas = response.data.response
                return 'hello'
            })
            .catch(error=>{
                        this.$q.notify({
                        message:error.message,
                        color: 'red',
                        type:'negative',
                        position:'top-right',
                        multiLine: true,
                        timeout:3000,
                        actions: [{ icon: 'close', color: 'white' }]
                      })
            })
        }
    }
})

export default AreaStore