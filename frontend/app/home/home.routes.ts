import { provideRouter, RouterConfig } from "@angular/router";
import { NotesListComponent } from "../notes/list/list.component";

const routes: RouterConfig = [
    {
        path: '',
        redirectTo: '/notes',
        pathMatch: 'full'
    },
    {
        path: 'notes',
        component: NotesListComponent
    }
];

export const appRouterProviders = [
    provideRouter(routes)
];