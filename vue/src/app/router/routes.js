import ListView from '@/app/views/ListView';
import UpdateView from '@/app/views/UpdateView';

const routes = [
    {
        path: '/',
        name: 'list',
        component: ListView,
    },
    {
        path: '/:id',
        name: 'retrieve',
        component: UpdateView,
    },
];

export default routes;
