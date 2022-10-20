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
              component: () => import( '@/views/admin/Vacancies.vue' )
            },
            {
              path: '/masters',
              name: 'masters',
              children:[
                  {
                    path: 'languages',
                    name: 'LanguagesMaster',
                    component: () => import( '@/components/admin/LanguagesMaster.vue' )
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