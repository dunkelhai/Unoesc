using Microsoft.VisualStudio.TestTools.UnitTesting;
using UNO.BL;


namespace UNO.BLTest
{
    [TestClass]
    public class OrderTest
    {
        [TestMethod]
        public void OrderValidation()
        {
            Order order = new Order(1);

            int expected = 1;

            int actual = order.OrderId;

            Assert.AreEqual(expected, actual);

            order.OrderDate = System.DateTimeOffset.Now;

            bool expected2 = true;

            bool actual2 = order.Validate();

            Assert.AreEqual(expected2, actual2);
            

        }
    }
}
