"use strict";
var platform_browser_dynamic_1 = require("@angular/platform-browser-dynamic");
var forms_1 = require('@angular/forms');
var http_1 = require('@angular/http');
var home_component_1 = require("./home/home.component");
var home_routes_1 = require("./home/home.routes");
platform_browser_dynamic_1.bootstrap(home_component_1.HomeComponent, [
    forms_1.disableDeprecatedForms(),
    forms_1.provideForms(),
    http_1.HTTP_PROVIDERS,
    home_routes_1.appRouterProviders
]);
//# sourceMappingURL=main.js.map