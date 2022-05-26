using Microsoft.VisualStudio.TestTools.UnitTesting;
using UNO.BL;


namespace UNO.BLTest
{
    [TestClass]
    public class OrderItemTest
    {
        [TestMethod]
        public void OrderItemValidation()
        {
            OrderItem orderItem = new OrderItem(1);

            //orderItem.Order
            //orderItem.Product

            orderItem.PurchasePrice = 100;
            orderItem.Quantity = 2;


            bool expected = true;

            bool actual = orderItem.Validate();

            Assert.AreEqual(expected, actual);

        }
    }
}
