using System;
namespace UNO.BL
{
    public class Order
    {
        public Order()
        {
        }
        public Order(int orderId)
        {
            OrderId = orderId;
        }

        public int OrderId { get; private set; }
        public DateTimeOffset OrderDate { get; set; }

        public bool Validate()
        {
            var isValid = true;

            if (OrderDate == null)
            {

                isValid = false;

            }


            return isValid;
        }
    }
}
