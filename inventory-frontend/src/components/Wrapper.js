import {Link} from "react-router-dom";

export const Wrapper = props => {
    return <>
    <header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
        <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="#">Shop</a>
        <button class="navbar-toggler position-absolute d-md-none collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="navbar-nav">
            <div class="nav-item text-nowrap">
                <a class="nav-link px-3" href="#">Sign out</a>
            </div>
        </div>
    </header>

        <div class="container-fluid">
            <div class="row">
                <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
                    <div class="position-sticky pt-3">
                        <ul class="nav flex-column">
                           
                            <li class="nav-item">
                                <a class="nav-link" href="#">
                                    <span data-feather="shopping-cart"></span>
                                    <Link to={"/"}>Products</Link>
                                </a>
                            </li>

                            <li class="nav-item">
                                <a class="nav-link" href="#">
                                    <span data-feather="shopping-cart"></span>
                                    <Link to={"/orders"}>Orders</Link>
                                </a>
                            </li>

                        </ul>


                    </div>
                </nav>

                <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                    {props.children}
                </main>
            </div>
        </div>

    </>
}