import React from 'react'
import Header from './header'
import Footer from './Footer'
import { ToastContainer} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Layout = ({children}) => {
  return (
    <div>
       <Header/>
        <main style={{minHeight:"85vh"}}>
          <ToastContainer />
          {children}
          </main>
        <Footer />
    </div>
  )
}

export default Layout