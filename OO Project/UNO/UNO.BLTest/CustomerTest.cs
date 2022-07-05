using Microsoft.VisualStudio.TestTools.UnitTesting;
using UNO.BL;


namespace UNO.BLTest
{
    [TestClass]
    public class CustomerTest
    {
        [TestMethod]
        public void FullNameValidation()
        {

            Customer customer = new Customer();
            customer.FirstName = "Alysson";
            customer.LastName = "Oliveira";

            string expected = "Oliveira, Alysson";

            string actual = customer.FullName;

            Assert.AreEqual(expected, actual);
            

        }
    }
}
