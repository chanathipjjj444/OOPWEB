import React from 'react'
import Layout from '../component/Layout/Layout'

const ManageUser = () => {
  return (
    <Layout title={"Dashboard - Create Category"}>
        <div className='container-fluid e-3 p-3'>

        <div className='row'>
            {/* <div className='col-md-3'>
                <AdminDashboard/>
            </div> */}
            <div className='col-md-9'>
                <h1>Manage Users</h1>
                {/* <div className='col-md-3'>
                    <CategoryForm 
                    handleSubmit={handleSubmit} 
                    value={name}
                    setValue={setName}
                    />
                </div> */}
                <div className='w-75'>
                <table className="table">
                <thead>
                    <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {/* {categories?.map((c)=>(
                        <>
                        <tr>
                        <td key={c._id}>{c.name}</td>
                        <td>
                            <div className="d-grid gap-3 d-md-flex justify-content-md">
                            <button className='btn btn-primary' onClick={()=> {setVisible(true) ; setUpdatedName(c.name); setSelected(c)}}>Edit</button>
                            <button className='btn btn-danger' onClick={()=> {handleDelete(c._id)}}>delete</button>
                            </div>
                        </td>
                        
                        </tr>
                        </>
                    
                    ))} */}
                        
                </tbody>
                </table>

                </div>
                {/* <Modal onCancel={()=> setVisible(false)} 
                footer={null} 
                visible={visible}
                >
                    <CategoryForm value={updatedName} setValue={setUpdatedName} handleSubmit={handleUpdate}></CategoryForm>
                </Modal> */}
            </div>
        </div>

        </div>
    </Layout>
  )
}

export default ManageUser