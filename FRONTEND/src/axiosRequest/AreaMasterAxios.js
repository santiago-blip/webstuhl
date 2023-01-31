import { useQuasar } from 'quasar'
import axios from 'axios'

const $q = useQuasar()

const requestArea = {
    'getAreas':   axios.get('http://127.0.0.1:8000/vacancies/master/areass/')
                        .then(response=>{
                        return response.data.response
                    })
                        .catch(error=>{
                                return $q.notify({
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

export default requestArea