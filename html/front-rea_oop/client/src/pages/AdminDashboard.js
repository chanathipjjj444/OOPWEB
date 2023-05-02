import Layout from '../component/Layout/Layout'
import React from 'react'
import { NavLink } from 'react-router-dom'

const AdminDashboard = () => {
  return (
    <Layout title="Admin">
    <div className='text-center'>
        <div className="list-group">
            <h4>Admin Panel</h4>
        <NavLink to="/admin/manage-hotel" className="list-group-item list-group-item-action">
            Manage 🏢Hotel
        </NavLink>
        <NavLink to="/admin/manage-room" className="list-group-item list-group-item-action">
            Manage room
        </NavLink>
        <NavLink to="/admin/manage-addons" className="list-group-item list-group-item-action">
            Manage addons
        </NavLink>
        </div>
    </div>
   </Layout>
  )
}

export default AdminDashboard