import VueRouter from "vue-router";
import AdminView from "@/components/AdminView"
import AdminUsers from "@/components/AdminUsers"
import AdminCustomers from "@/components/AdminCustomers"
import EditUser from "@/components/EditUser"
import CreateCustomer from "@/components/CreateCustomer"

const admin_routes = [
  {
    path: "/admin",
    name: "Admin",
    component: AdminView,
  },
  {
    path: "/admin/users",
    name: "Users",
    component: AdminUsers,
  },
  {
    path: "/admin/customers",
    name: "Customers",
    component: AdminCustomers,
  },
  {
    path: "/admin/users/edit/:username",
    name: "Add user",
    component: EditUser,
  },
  {
    path: "/admin/customers/new",
    name: "Add customer",
    component: CreateCustomer,
  }
]

export const admin_router = new VueRouter({
  mode: "history",
  routes: admin_routes,
})
