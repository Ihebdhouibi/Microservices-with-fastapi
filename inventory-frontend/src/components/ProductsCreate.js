export const ProductsCreate = () => {
    return <form className="mt-3">
        <div className="form-floating pb-3">
            <input className="form-control" placeholder="Name" />
            <label>Name</label>
        </div>
        <div className="form-floating pb-3">
            <input className="form-control" placeholder="Price" />
            <label>Price</label>
        </div>
        <div className="form-floating pb-3">
            <input className="form-control" placeholder="Quantity" />
            <label>Quantity</label>
        </div>
            <button className="btn w-100 btn-lg btn-primary" type="submit">Submit</button>

    </form>
}