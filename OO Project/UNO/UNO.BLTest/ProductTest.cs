using Microsoft.VisualStudio.TestTools.UnitTesting;
using UNO.BL;


namespace UNO.BLTest
{
    [TestClass]
    public class ProductTest
    {
        [TestMethod]
        public void ProductValidation()
        {
            Product product = new Product(1);

            product.ProductName = "Meia cano curto";
            product.ProductDescription = "Usar no pé";
            product.CurrentPrice = 30;


            bool expected = true;

            bool actual = product.Validate();

            Assert.AreEqual(expected, actual);

        }
    }
}
