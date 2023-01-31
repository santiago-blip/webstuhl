import { createRouter, createWebHistory } from 'vue-router'

//Protect routes doc: https://router.vuejs.org/guide/advanced/navigation-guards.html#global-after-hooks
const parseJwt = (token) => {
  var base64Url = token.split('.')[1];
  var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
  var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }).join(''));

  return JSON.parse(jsonPayload);
}


const routes = [
    {
        path: '/',
        name: 'landing',
        component: () => import( '@/views/public/Landing.vue' )
    },
    {
        path: '/admin',
        name: 'admin',
        component: () => import( '@/views/admin/Administration.vue' ),
        beforeEnter: (to, from,next) => {
          const tokenAccess = JSON.parse(sessionStorage.getItem('tokens'))
          if (!tokenAccess) return next({name:'landing'})
          if(!parseJwt(tokenAccess.access).superUser)return next({name:'landing'})
          return next()
        },
        children:[
            {
              path: 'vacancies',
              name: 'vacancies',
              component: () => import( '@/views/admin/VacanciesView.vue' )
            },
            {
              path: '/masters',
              name: 'masters',
              children:[
                  {
                    path: 'languages',
                    name: 'languagesMaster',
                    component: () => import( '@/views/admin/masters/LanguagesMasterView.vue' )
                  },
                  {
                    path: 'languages-levels',
                    name: 'languagesLevelsMaster',
                    component: () => import( '@/views/admin/masters/LanguagesLevelsMasterView.vue' )
                  },
                  {
                    path: 'areas',
                    name: 'areasMaster',
                    component: () => import( '@/views/admin/masters/AreasMasterView.vue' )
                  },
                  {
                    path: 'levels',
                    name: 'levelsMaster',
                    component: () => import( '@/views/admin/masters/LevelsMasterView.vue' )
                  },
                  {
                    path: 'professions',
                    name: 'professionsMaster',
                    component: () => import( '@/views/admin/masters/ProfessionsMasterView.vue' )
                  },
                  {
                    path: 'professionsDegree',
                    name: 'professionsDegreeMaster',
                    component: () => import( '@/views/admin/masters/ProfessionsDegreeMasterView.vue' )
                  },
                  {
                    path: 'internal-contact',
                    name: 'InternalContactMaster',
                    component: () => import( '@/views/admin/masters/InternalContactMasterView.vue' )
                  },
                  {
                    path: 'internal-contact-objetive',
                    name: 'InternalContactObjetiveMaster',
                    component: () => import( '@/views/admin/masters/InternalContactObjetiveMasterView.vue' )
                  },
                  {
                    path: 'external-contact',
                    name: 'ExternalContactMaster',
                    component: () => import( '@/views/admin/masters/ExternalContactMasterView.vue' )
                  },
                  {
                    path: 'external-contact-objetive',
                    name: 'ExternalContactObjetiveMaster',
                    component: () => import( '@/views/admin/masters/ExternalContactObjetiveMasterView.vue' )
                  }
                ]
            },
        ]
    },
    {
      path: '/details/:id',
      name: 'details',
      component: () => import( '@/views/public/VacanciesDetails.vue')
  }
]

const router=createRouter({
    history: createWebHistory(),
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
          return savedPosition
        } else {
          return { top: 0 }
        }
      },
    
    routes 
})

export default router