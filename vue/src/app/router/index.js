import routes from '@/app/router/routes';
import { createRouter, createWebHashHistory } from 'vue-router';

const router = createRouter({
    history: createWebHashHistory(),
    base: '/vue/',
    routes: routes,
});

export default router;
